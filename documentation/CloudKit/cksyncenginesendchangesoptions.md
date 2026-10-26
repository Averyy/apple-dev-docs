# CKSyncEngineSendChangesOptions

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

A set of options to use with a send operation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface CKSyncEngineSendChangesOptions : NSObject
```

## Topics

### Managing attributes
- [operationGroup](./cksyncenginesendchangesoptions/operationgroup.md)
  The operation group to use for the underlying CloudKit operations.
### Instance Properties
- [scope](./cksyncenginesendchangesoptions/scope.md)
  The scope in which to send changes to the server.
### Instance Methods
- [- initWithScope:](./cksyncenginesendchangesoptions/initwithscope_.md)
  Initializes a set of options with the specific scope.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Invoking manual sync operations
- [- fetchChangesWithCompletionHandler:](./cksyncengine-4b4w9/fetchchangeswithcompletionhandler_.md)
  Fetches pending remote changes from the server.
- [- fetchChangesWithOptions:completionHandler:](./cksyncengine-4b4w9/fetchchangeswithoptions_completionhandler_.md)
  Fetches pending remote changes from the server using the specified options.
- [CKSyncEngineFetchChangesOptions](./cksyncenginefetchchangesoptions.md)
  A set of options to use with a fetch operation.
- [- sendChangesWithCompletionHandler:](./cksyncengine-4b4w9/sendchangeswithcompletionhandler_.md)
  Sends pending local changes to the server.
- [- sendChangesWithOptions:completionHandler:](./cksyncengine-4b4w9/sendchangeswithoptions_completionhandler_.md)
  Sends pending local changes to the server using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesendchangesoptions)*