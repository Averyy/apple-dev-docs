# init(_:)

**Framework**: Swift  
**Kind**: init

Initializes every element in this array, by calling the given closure with each index.

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
init<E>(_ body: (InlineArray<count, Element>.Index) throws(E) -> Element) throws(E) where E : Error
```

#### Discussion

This will call the closure `count` times, where `count` is the static count of the array, to initialize every element by passing the closure the index of the current element being initialized.

```swift
InlineArray<4, Int> { 1 << $0 }  //-> [1, 2, 4, 8]
```

The closure is allowed to throw an error at any point during initialization at which point the array will stop initialization, deinitialize every currently initialized element, and throw the given error back out to the caller.

> **Note**: O(), where  is the number of elements in the array.

## Parameters

- `body`: A closure that returns an owned   to emplace at   the passed in index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/inlinearray/init(_:))*