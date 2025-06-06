# init(shareURLs:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for fetching the metadata for the specified shares.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(shareURLs: [URL])
```

#### Discussion

After creating the operation, assign a handler to the [`fetchShareMetadataCompletionBlock`](ckfetchsharemetadataoperation/fetchsharemetadatacompletionblock.md) property to process the results.

## Parameters

- `shareURLs`: The URLs of the shares. If you specify  , you must assign a value to the   property before you execute the operation.

## See Also

- [init()](ckfetchsharemetadataoperation/init.md)
  Creates an empty fetch share metadata operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/init(shareurls:))*