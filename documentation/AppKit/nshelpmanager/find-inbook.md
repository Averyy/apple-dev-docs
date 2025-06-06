# find(_:inBook:)

**Framework**: AppKit  
**Kind**: method

Performs a search for the specified string in the specified book.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func find(_ query: String, inBook book: NSHelpManager.BookName?)
```

#### Discussion

To search for a string in your bundle’s localized help book, you could use code similar to the following:

```objc
NSString *locBookName = [[NSBundle mainBundle] objectForInfoDictionaryKey: @"CFBundleHelpBookName"];
[[NSHelpManager sharedHelpManager] findString:@"Hello"  inBook:locBookName];
```

This is a wrapper for `AHRegisterHelpBook` (which is called only once to register the help book specified in the application’s main bundle) and `AHSearch`.

## Parameters

- `query`: String to search for.
- `book`: Localized help book to search. When  , all installed help books are searched.

## See Also

- [func openHelpAnchor(NSHelpManager.AnchorName, inBook: NSHelpManager.BookName?)](nshelpmanager/openhelpanchor(_:inbook:).md)
  Finds and displays the text at the given anchor location in the given book.
- [NSHelpManager.AnchorName](nshelpmanager/anchorname.md)
- [NSHelpManager.BookName](nshelpmanager/bookname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/find(_:inbook:))*