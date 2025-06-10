# init(first:next:)

**Framework**: Swift  
**Kind**: init

Initializes every element in this array, by calling the given closure with each preceding element.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init<E>(first: consuming Element, next: (borrowing Element) throws(E) -> Element) throws(E) where E : Error
```

#### Discussion

This will call the closure `count - 1` times, where `count` is the static count of the array, to initialize every element by passing the closure an immutable borrow reference to the preceding element.

```swift
InlineArray<4, Int>(first: 1) { $0 << 1 }  //-> [1, 2, 4, 8]
```

The closure is allowed to throw an error at any point during initialization at which point the array will stop initialization, deinitialize every currently initialized element, and throw the given error back out to the caller.

> **Note**: O(), where  is the number of elements in the array.

## Parameters

- `first`: The first value to emplace into the array.
- `next`: A closure that takes an immutable borrow reference to the   preceding element, and returns an owned   instance to emplace   into the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/inlinearray/init(first:next:))*