# name

**Framework**: Swift  
**Kind**: property

Returns the human-readable name of the current task, if it was set during the tasks’ creation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var name: String? { get }
```

#### Discussion

Tasks can be named during their creation, which can be helpful to identify unique tasks which may be created at same source locations, for example:

```swift
func process(items: [Int]) async {
  await withTaskGroup { group in
    for item in items {
      group.addTask(name: "process-\(item)") {
        await process(item)
      }
    }
  }
}
```

##### Task Name Availability

The task name is only available when running with a recent runtime (Swift 6.2+).

[`Task`](task.md) initializers which may accept a task name are more available than this property, for convenience purposes, in order to not have to set task names conditionally however their effect is runtime dependent, and is reflected in the availability of this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/name)*