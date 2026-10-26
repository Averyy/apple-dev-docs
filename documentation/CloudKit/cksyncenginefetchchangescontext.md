# CKSyncEngineFetchChangesContext

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

The context of an attempt to fetch changes from the server.

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
@interface CKSyncEngineFetchChangesContext : NSObject
```

#### Overview

The sync engine might attempt to fetch changes from the server for many reasons. For example, if you call [`fetchChangesWithCompletionHandler:`](./cksyncengine-4b4w9/fetchchangeswithcompletionhandler_.md), it tries to fetch changes immediately. Or if it receives a push notification, it schedules a sync and fetch changes when the scheduler task runs.

## Topics

### Instance Properties
- [options](./cksyncenginefetchchangescontext/options.md)
  The options being used for this attempt to fetch changes.
- [reason](./cksyncenginefetchchangescontext/reason.md)
  The reason why the sync engine is attempting to fetch changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginefetchchangescontext)*