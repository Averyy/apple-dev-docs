# objectAfterChanges

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

An object that reflects the current state of the asset or collection it represents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var objectAfterChanges: ObjectType? { get }
```

```objc
@property (atomic, strong, readonly, nullable) ObjectType objectAfterChanges;
```

## Discussion

Read this object’s properties to retrieve updated metadata for the asset or collection. Using this object is equivalent to repeating the same fetch that returned the original object.

## See Also

### Getting the Changed Object
- [var objectBeforeChanges: ObjectType](./objectbeforechanges.md)
  An object that reflects the original state of the asset or collection it represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phobjectchangedetails/objectafterchanges)*