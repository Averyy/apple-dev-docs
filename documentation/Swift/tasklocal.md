# TaskLocal

**Framework**: Swift  
**Kind**: class

Wrapper type that defines a task-local value key.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
final class TaskLocal<Value> where Value : Sendable
```

#### Overview

A task-local value is a value that can be bound and read in the context of a [`Task`](task.md). It is implicitly carried with the task, and is accessible by any child tasks it creates (such as TaskGroup or `async let` created tasks).

##### Task Local Declarations

Task locals must be declared as static properties or global properties, like this:

```swift
enum Example {
    @TaskLocal
    static var traceID: TraceID?
}

// Global task local properties are supported since Swift 6.0:
@TaskLocal
var contextualNumber: Int = 12
```

##### Default Values

Reading a task local value when no value was bound to it results in returning its default value. For a task local declared as optional (such as e.g. `TraceID?`), this defaults to nil, however a different default value may be defined at declaration site of the task local, like this:

```swift
enum Example { 
    @TaskLocal
    static var traceID: TraceID = TraceID.default
}
```

The default value is returned whenever the task-local is read from a context which either: has no task available to read the value from (e.g. a synchronous function, called without any asynchronous function in its call stack), or no value was bound within the scope of the current task or any of its parent tasks.

##### Reading Task Local Values

Reading task local values is simple and looks the same as-if reading a normal static property:

```swift
guard let traceID = Example.traceID else {
  print("no trace id")
  return
}
print(traceID)
```

It is possible to perform task-local value reads from either asynchronous or synchronous functions.

##### Binding Task Local Values

Task local values cannot be `set` directly and must instead be bound using the scoped `$traceID.withValue() { ... }` operation. The value is only bound for the duration of that scope, and is available to any child tasks which are created within that scope.

Detached tasks do not inherit task-local values, however tasks created using the `Task { ... }` initializer do inherit task-locals by copying them to the new asynchronous task, even though it is an un-structured task.

##### Using Task Local Values Outside of Tasks

It is possible to bind and read task local values outside of tasks.

This comes in handy within synchronous functions which are not guaranteed to be called from within a task. When binding a task-local value from outside of a task, the runtime will set a thread-local in which the same storage mechanism as used within tasks will be used. This means that you can reliably bind and read task local values without having to worry about the specific calling context, e.g.:

```swift
func enter() {
    Example.$traceID.withValue("1234") {
        read() // always "1234", regardless if enter() was called from inside a task or not:
}

func read() -> String {
    if let value = Self.traceID {
        "\(value)" 
    } else { 
        "<no value>"
    }
}

// 1) Call `enter` from non-Task code
//    e.g. synchronous main() or non-Task thread (e.g. a plain pthread)
enter()

// 2) Call 'enter' from Task
Task { 
    enter()
}
```

In either cases listed above, the binding and reading of the task-local value works as expected.

##### Examples

```swift
enum Example {
    @TaskLocal
    static var traceID: TraceID?
}

func read() -> String {
    if let value = Self.traceID {
        "\(value)" 
    } else { 
        "<no value>"
    }
}

await Example.$traceID.withValue(1234) { // bind the value
  print("traceID: \(Example.traceID)") // traceID: 1234
  read() // traceID: 1234

  async let id = read() // async let child task, traceID: 1234

  await withTaskGroup(of: String.self) { group in 
      group.addTask { read() } // task group child task, traceID: 1234
      return await group.next()!
  }

  Task { // unstructured tasks do inherit task locals by copying
    read() // traceID: 1234
  }

  Task.detached { // detached tasks do not inherit task-local values
    read() // traceID: nil
  }
}
```

> **Note**: `TaskLocal-macro`

## Topics

### Initializers
- [init(wrappedValue: Value)](tasklocal/init(wrappedvalue:).md)
### Instance Properties
- [var description: String](tasklocal/description.md)
  A textual representation of this instance.
- [var projectedValue: TaskLocal<Value>](tasklocal/projectedvalue.md)
- [var wrappedValue: Value](tasklocal/wrappedvalue.md)
### Instance Methods
- [func get() -> Value](tasklocal/get.md)
  Gets the value currently bound to this task-local from the current task.
- [func withValue<R>(Value, operation: () throws -> R, file: String, line: UInt) rethrows -> R](tasklocal/withvalue(_:operation:file:line:).md)
  Binds the task-local to the specific value for the duration of the synchronous operation.
- [func withValue<R>(Value, operation: () async throws -> R, isolation: isolated (any Actor)?, file: String, line: UInt) async rethrows -> R](tasklocal/withvalue(_:operation:isolation:file:line:).md)
  Binds the task-local to the specific value for the duration of the asynchronous operation.

## Relationships

### Conforms To
- [CustomStringConvertible](customstringconvertible.md)
- [Sendable](sendable.md)

## See Also

- [macro TaskLocal()](tasklocal().md)
  Macro that introduces a [`TaskLocal`](tasklocal.md) binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Swift/tasklocal)*