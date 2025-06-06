# removeAll(keepingCapacity:)

**Framework**: System  
**Kind**: method

Removes all elements from the collection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
mutating func removeAll(keepingCapacity keepCapacity: Bool = false)
```

#### Discussion

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O(), where  is the length of the collection.

## Parameters

- `keepCapacity`: Pass   to request that the collection   avoid releasing its storage. Retaining the collection’s storage can   be a useful optimization when you’re planning to grow the collection   again. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/removeall(keepingcapacity:))*