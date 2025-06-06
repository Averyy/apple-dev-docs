# assertNoFailure(_:file:line:)

**Framework**: Combine  
**Kind**: method

Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.

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
func assertNoFailure(_ prefix: String = "", file: StaticString = #file, line: UInt = #line) -> Publishers.AssertNoFailure<Self>
```

#### Return Value

A publisher that raises a fatal error when its upstream publisher fails.

#### Discussion

Use `assertNoFailure()` for internal integrity checks that are active during testing. However, it is important to note that, like its Swift counterpart `fatalError(_:)`, the `assertNoFailure()` operator asserts a fatal exception when triggered during development and testing,  in shipping versions of code.

In the example below, a `CurrentValueSubject` publishes the initial and second values successfully. The third value, containing a `genericSubjectError`, causes the `assertNoFailure()` operator to assert a fatal exception stopping the process:

```swift
public enum SubjectError: Error {
    case genericSubjectError
}

let subject = CurrentValueSubject<String, Error>("initial value")
subject
    .assertNoFailure()
    .sink(receiveCompletion: { print ("completion: \($0)") },
          receiveValue: { print ("value: \($0).") }
    )

subject.send("second value")
subject.send(completion: Subscribers.Completion<Error>.failure(SubjectError.genericSubjectError))

// Prints:
//  value: initial value.
//  value: second value.
//  The process then terminates in the debugger as the assertNoFailure operator catches the genericSubjectError.
```

## Parameters

- `prefix`: A string used at the beginning of the fatal error message.
- `file`: A filename used in the error message. This defaults to  .
- `line`: A line number used in the error message. This defaults to  .

## See Also

- [func `catch`<P>((Self.Failure) -> P) -> Publishers.Catch<Self, P>](publishers/mapkeypath2/catch(_:).md)
  Handles errors from an upstream publisher by replacing it with another publisher.
- [func tryCatch<P>((Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P>](publishers/mapkeypath2/trycatch(_:).md)
  Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [func retry(Int) -> Publishers.Retry<Self>](publishers/mapkeypath2/retry(_:).md)
  Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/mapkeypath2/assertnofailure(_:file:line:))*