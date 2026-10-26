# delegate

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The object that provides the records to sync and handles any related events.

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
@property (weak) id<CKSyncEngineDelegate> delegate;
```

## See Also

### Handling record changes
- [CKSyncEngineDelegate](../cksyncenginedelegate-3c38p.md)
  An interface for providing record data to a sync engine and customizing that engine’s behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineconfiguration/delegate)*