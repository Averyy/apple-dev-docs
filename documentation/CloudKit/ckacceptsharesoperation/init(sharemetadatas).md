# init(shareMetadatas:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates an operation for accepting the specified shares.

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
convenience init(shareMetadatas: [CKShare.Metadata])
```

```objc
- (instancetype) initWithShareMetadatas:(NSArray<CKShareMetadata *> *) shareMetadatas;
```

#### Discussion

After initializing the operation, assign a handler to the [`acceptSharesCompletionBlock`](./acceptsharescompletionblock.md) property to process the results.

## Parameters

- `shareMetadatas`: The share metadatas to accept. If you specify `nil`, you must assign a value to the [`shareMetadatas`](./sharemetadatas.md) property before you execute the operation.

## See Also

### Creating a Share Accept Operation
- [init()](./init%28%29.md)
  Creates an operation for accepting shares.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/init(sharemetadatas:))*