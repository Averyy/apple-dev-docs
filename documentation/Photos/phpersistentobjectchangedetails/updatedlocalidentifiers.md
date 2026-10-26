# updatedLocalIdentifiers

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The local identifiers the system updates since the change token you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var updatedLocalIdentifiers: Set<String> { get }
```

```objc
@property (nonatomic, strong, readonly) NSSet<NSString *> * updatedLocalIdentifiers;
```

#### Discussion

This value includes assets the user moves to the trash or hides, so they may later be available if the user removes an asset from the trash or unhides it.

## See Also

### Getting the Change Details
- [var insertedLocalIdentifiers: Set<String>](./insertedlocalidentifiers.md)
  The local identifiers the system inserts since the change token you specify.
- [var deletedLocalIdentifiers: Set<String>](./deletedlocalidentifiers.md)
  The local identifiers the system deletes since the change token you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phpersistentobjectchangedetails/updatedlocalidentifiers)*