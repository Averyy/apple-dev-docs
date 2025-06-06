# removeAll(keepingCapacity:)

**Framework**: Swift  
**Kind**: method

Removes all elements from the collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func removeAll(keepingCapacity keepCapacity: Bool = false)
```

#### Discussion

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O(), where  is the length of the collection.

O(), where  is the length of the collection.

## Parameters

- `keepCapacity`: Pass   to request that the collection   avoid releasing its storage. Retaining the collection’s storage can   be a useful optimization when you’re planning to grow the collection   again. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/removeall(keepingcapacity:))*