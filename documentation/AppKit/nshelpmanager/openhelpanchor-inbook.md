# openHelpAnchor(_:inBook:)

**Framework**: AppKit  
**Kind**: method

Finds and displays the text at the given anchor location in the given book.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func openHelpAnchor(_ anchor: NSHelpManager.AnchorName, inBook book: NSHelpManager.BookName?)
```

#### Discussion

To open an anchor in your bundle’s localized help book, you could use code similar to the following:

```objc
NSString *locBookName = [[NSBundle mainBundle] objectForInfoDictionaryKey: @"CFBundleHelpBookName"];
[[NSHelpManager sharedHelpManager] openHelpAnchor:@"anchor1"  inBook:locBookName];
```

This method is a wrapper for `AHRegisterHelpBook` (which is called only once to register the help book specified in the application’s main bundle) and `AHLookupAnchor`.

## Parameters

- `anchor`: Location of the desired text.
- `book`: Help book containing the anchor. When  , all installed help books are searched.

## See Also

- [func find(String, inBook: NSHelpManager.BookName?)](nshelpmanager/find(_:inbook:).md)
  Performs a search for the specified string in the specified book.
- [NSHelpManager.AnchorName](nshelpmanager/anchorname.md)
- [NSHelpManager.BookName](nshelpmanager/bookname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/openhelpanchor(_:inbook:))*