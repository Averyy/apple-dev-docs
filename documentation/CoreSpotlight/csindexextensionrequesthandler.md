# CSIndexExtensionRequestHandler

**Framework**: Core Spotlight  
**Kind**: class  
**Role**: Class

An interface that implements an index-maintenance app extension.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class CSIndexExtensionRequestHandler
```

```objc
@interface CSIndexExtensionRequestHandler : NSObject
```

## Mentions

- [Generating summary and priority data for indexed items](./generating-summary-and-priority-data-for-indexed-items.md)

#### Overview

The `CSIndexExtensionRequestHandler` class provides the main entry point for an index-maintenance app extension. If any issues arise with your app’s indexes and your app isn’t running, the system loads your app extension and looks for an implementation of this class. It instantiates the class it finds and uses it to perform any index-related maintenance.

Define a custom subclass of `CSIndexExtensionRequestHandler` in your app extension and implement methods of the [`CSSearchableIndexDelegate`](./cssearchableindexdelegate.md) protocol in it. Use those methods to perform any required updates to your app’s index files. For example, use the [`searchableIndex(_:reindexAllSearchableItemsWithAcknowledgementHandler:)`](./cssearchableindexdelegate/searchableindex%28_,reindexallsearchableitemswithacknowledgementhandler%29.md) method to reindex all items in your app.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CSSearchableIndexDelegate](./cssearchableindexdelegate.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Spotlight app extensions
- [Regenerating your app’s indexes on demand](./regenerating-your-app-s-indexes-on-demand.md)
  Create an app extension to maintain your app’s indexes and regenerate them as needed.
- [class CSImportExtension](./csimportextension.md)
  An object that provides searchable attributes for file types that the app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csindexextensionrequesthandler)*