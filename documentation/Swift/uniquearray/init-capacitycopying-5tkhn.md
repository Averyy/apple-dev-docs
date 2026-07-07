# init(capacity:copying:)

**Framework**: Swift  
**Kind**: init

Creates a new array with the specified initial capacity, holding a copy of the contents of a given sequence.

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
init(capacity: Int? = nil, copying contents: some Sequence<Element>)
```

## Parameters

- `capacity`: The storage capacity of the new array, or nil to allocate just enough capacity to store the contents.
- `contents`: The sequence whose contents to copy into the new array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/init(capacity:copying:)-5tkhn)*