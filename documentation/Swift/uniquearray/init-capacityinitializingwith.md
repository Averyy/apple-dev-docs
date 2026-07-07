# init(capacity:initializingWith:)

**Framework**: Swift  
**Kind**: init

Creates a new array with the specified capacity, directly initializing its storage using an output span.

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
init<E>(capacity: Int, initializingWith body: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `capacity`: The storage capacity of the new array.
- `body`: A callback that gets called at most once to directly populate newly reserved storage within the array. The function is allowed to add fewer than `capacity` items. The array is initialized with however many items the callback adds to the output span before it returns (or before it throws an error).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/init(capacity:initializingwith:))*