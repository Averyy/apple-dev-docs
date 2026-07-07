# edit(_:)

**Framework**: Swift  
**Kind**: method

Arbitrarily edit the storage underlying this array by invoking a user-supplied closure with a mutable `OutputSpan` view over it. This method calls its function argument at most once, allowing it to arbitrarily modify the contents of the output span it is given. The argument is free to add, remove or reorder any items; however, it is not allowed to replace the span or change its capacity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
mutating func edit<E, R>(_ body: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Return Value

This method returns the result of its function argument.

#### Discussion

When the function argument finishes (whether by returning or throwing an error) the rigid array instance is updated to match the final contents of the output span.

> **Note**: Adds O(1) overhead to the complexity of the function argument.

## Parameters

- `body`: A function that edits the contents of this array through an `OutputSpan` argument. This method invokes this function at most once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/edit(_:))*