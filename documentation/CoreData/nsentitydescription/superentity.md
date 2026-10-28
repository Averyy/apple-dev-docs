# superentity

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The super-entity of the receiver.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
unowned(unsafe) var superentity: NSEntityDescription? { get }
```

```objc
@property (assign, readonly, nullable) NSEntityDescription * superentity;
```

## Discussion

If the receiver has no super-entity, returns `nil`.

## See Also

### Managing inheritance
- [var subentitiesByName: [String : NSEntityDescription]](./subentitiesbyname.md)
  A dictionary containing the receiver’s sub-entities.
- [var subentities: [NSEntityDescription]](./subentities.md)
  An array containing the sub-entities of the receiver.
- [func isKindOf(entity: NSEntityDescription) -> Bool](./iskindof%28entity%29.md)
  Returns a Boolean value that indicates whether the receiver is a sub-entity of another given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/superentity)*