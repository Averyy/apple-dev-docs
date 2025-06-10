# WebHistoryItemsAdded

**Framework**: Foundation  
**Kind**: property

Posted when history items have been added to a web history.

**Availability**:
- macOS 10.3+

## Declaration

```swift
static let WebHistoryItemsAdded: NSNotification.Name
```

#### Discussion

The notification object is the web history to which the items were added. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| @“WebHistoryItemsKey” | An [`NSArray`](nsarray.md) object containing the added items. |

## See Also

- [func addItems([Any]!)](../webkit/webhistory/1521407-additems.md)
  Inserts or updates the specified items in the web history.
- [static let WebHistoryAllItemsRemoved: NSNotification.Name](nsnotification/name-swift.struct/webhistoryallitemsremoved.md)
  Posted when all history items have been removed from the web history.
- [static let WebHistoryItemChanged: NSNotification.Name](nsnotification/name-swift.struct/webhistoryitemchanged.md)
  Posted by a WebHistoryItem object when the value of the history item’s title, alternate title, URL strings, or last visited interval changes.
- [static let WebHistoryItemsRemoved: NSNotification.Name](nsnotification/name-swift.struct/webhistoryitemsremoved.md)
  Posted when items have been removed from the web history.
- [static let WebHistoryLoaded: NSNotification.Name](nsnotification/name-swift.struct/webhistoryloaded.md)
  Posted when web history items have been loaded from a URL.
- [static let WebHistorySaved: NSNotification.Name](nsnotification/name-swift.struct/webhistorysaved.md)
  Posted when web history items have been saved to a URL.
- [static let WebPreferencesChanged: NSNotification.Name](nsnotification/name-swift.struct/webpreferenceschanged.md)
  Posted when the web preference settings are changed.
- [static let WebViewDidBeginEditing: NSNotification.Name](nsnotification/name-swift.struct/webviewdidbeginediting.md)
  Posted when a web view begins any operation that changes its contents in response to user editing.
- [static let WebViewDidChange: NSNotification.Name](nsnotification/name-swift.struct/webviewdidchange.md)
  Posted when a web view performs any operation that changes its contents in response to user editing.
- [static let WebViewDidChangeSelection: NSNotification.Name](nsnotification/name-swift.struct/webviewdidchangeselection.md)
  Posted when a web view changes its typing selection.
- [static let WebViewDidChangeTypingStyle: NSNotification.Name](nsnotification/name-swift.struct/webviewdidchangetypingstyle.md)
  Posted when a web view changes its typing style.
- [static let WebViewDidEndEditing: NSNotification.Name](nsnotification/name-swift.struct/webviewdidendediting.md)
  Posted when a web view ends any operation that changes its contents in response to user editing.
- [static let WebViewProgressEstimateChanged: NSNotification.Name](nsnotification/name-swift.struct/webviewprogressestimatechanged.md)
  Posted by a WebView object when the estimated progress value of a load changes.
- [static let WebViewProgressFinished: NSNotification.Name](nsnotification/name-swift.struct/webviewprogressfinished.md)
  Posted by a WebView object when the load has finished.
- [static let WebViewProgressStarted: NSNotification.Name](nsnotification/name-swift.struct/webviewprogressstarted.md)
  Posted by a WebView object when a load begins, including a load that is initiated in a subframe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/webhistoryitemsadded)*