# WebHistoryLoaded

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Posted when web history items have been loaded from a URL.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
static let WebHistoryLoaded: NSNotification.Name
```

## Discussion

The notification object is the web history that loaded the history items. This notification does not contain a `userInfo` dictionary.

## See Also

### Related Documentation
- [func load(from: URL!) throws](../../../WebKit/webhistory/load%28from%29.md)
  Loads the contents of the specified web history file.
### WebKit
- [static let WebHistoryAllItemsRemoved: NSNotification.Name](./webhistoryallitemsremoved.md)
  Posted when all history items have been removed from the web history.
- [static let WebHistoryItemChanged: NSNotification.Name](./webhistoryitemchanged.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.
- [static let WebHistoryItemsAdded: NSNotification.Name](./webhistoryitemsadded.md)
  Posted when history items have been added to a web history.
- [static let WebHistoryItemsRemoved: NSNotification.Name](./webhistoryitemsremoved.md)
  Posted when items have been removed from the web history.
- [static let WebHistorySaved: NSNotification.Name](./webhistorysaved.md)
  Posted when web history items have been saved to a URL.
- [static let WebPreferencesChanged: NSNotification.Name](./webpreferenceschanged.md)
  Posted when the web preference settings are changed.
- [static let WebViewDidBeginEditing: NSNotification.Name](./webviewdidbeginediting.md)
  Posted when a web view begins any operation that changes its contents in response to user editing.
- [static let WebViewDidChange: NSNotification.Name](./webviewdidchange.md)
  Posted when a web view performs any operation that changes its contents in response to user editing.
- [static let WebViewDidChangeSelection: NSNotification.Name](./webviewdidchangeselection.md)
  Posted when a web view changes its typing selection.
- [static let WebViewDidChangeTypingStyle: NSNotification.Name](./webviewdidchangetypingstyle.md)
  Posted when a web view changes its typing style.
- [static let WebViewDidEndEditing: NSNotification.Name](./webviewdidendediting.md)
  Posted when a web view ends any operation that changes its contents in response to user editing.
- [static let WebViewProgressEstimateChanged: NSNotification.Name](./webviewprogressestimatechanged.md)
  Posted by a WebView object when the estimated progress value of a load changes.
- [static let WebViewProgressFinished: NSNotification.Name](./webviewprogressfinished.md)
  Posted by a WebView object when the load has finished.
- [static let WebViewProgressStarted: NSNotification.Name](./webviewprogressstarted.md)
  Posted by a WebView object when a load begins, including a load that is initiated in a subframe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/webhistoryloaded)*