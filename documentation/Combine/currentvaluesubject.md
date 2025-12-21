# CurrentValueSubject

**Framework**: Combine  
**Kind**: class

A subject that wraps a single value and publishes a new element whenever the value changes.

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
final class CurrentValueSubject<Output, Failure> where Failure : Error
```

## Mentions

- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)

#### Overview

Unlike [`PassthroughSubject`](passthroughsubject.md), [`CurrentValueSubject`](currentvaluesubject.md) maintains a buffer of the most recently published element.

Calling [`send(_:)`](subject/send(_:).md) on a [`CurrentValueSubject`](currentvaluesubject.md) also updates the current value, making it equivalent to updating the [`value`](currentvaluesubject/value.md) directly.

## Topics

### Creating a current value subject
- [init(Output)](currentvaluesubject/init(_:).md)
  Creates a current value subject with the given initial value.
### Accessing the current value
- [var value: Output](currentvaluesubject/value.md)
  The value wrapped by this subject, published as a new element whenever it changes.

## Relationships

### Conforms To
- [Publisher](publisher.md)
- [Subject](subject.md)

## See Also

- [protocol Subject](subject.md)
  A publisher that exposes a method for outside callers to publish elements.
- [class PassthroughSubject](passthroughsubject.md)
  A subject that broadcasts elements to downstream subscribers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/currentvaluesubject)*