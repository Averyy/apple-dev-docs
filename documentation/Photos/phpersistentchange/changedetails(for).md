# changeDetails(for:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns the change history that contains the local identifiers for object inserts, updates, and deletes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func changeDetails(for objectType: PHObjectType) throws -> PHPersistentObjectChangeDetails
```

```objc
- (PHPersistentObjectChangeDetails *) changeDetailsForObjectType:(PHObjectType) objectType error:(NSError **) error;
```

## Return Value

An object that represents the change details.

## Parameters

- `objectType`: The type of object to request change details for.

## See Also

### Getting the Change History
- [class PHPersistentObjectChangeDetails](../phpersistentobjectchangedetails.md)
  An object that represents the local identifiers that change between requests using a change token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phpersistentchange/changedetails(for:))*