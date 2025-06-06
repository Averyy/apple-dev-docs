# CollectionDifference.Change.insert(offset:element:associatedWith:)

**Framework**: Swift  
**Kind**: case

An insertion.

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
case insert(offset: Int, element: ChangeElement, associatedWith: Int?)
```

#### Discussion

The `offset` value is the offset of the inserted element in the final state of the collection after the difference is fully applied. A non-`nil` `associatedWith` value is the offset of the complementary change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectiondifference/change/insert(offset:element:associatedwith:))*