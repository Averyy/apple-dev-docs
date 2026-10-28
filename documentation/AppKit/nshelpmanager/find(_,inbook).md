# find(_:inBook:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs a search for the specified string in the specified book.

**Availability**:
- macOS

## Declaration

```swift
func find(_ query: String, inBook book: NSHelpManager.BookName?)
```

```objc
- (void) findString:(NSString *) query inBook:(NSHelpBookName) book;
```

## Discussion

To search for a string in your bundle’s localized help book, you could use code similar to the following:

```objc
NSString *locBookName = [[NSBundle mainBundle] objectForInfoDictionaryKey: @"CFBundleHelpBookName"];
[[NSHelpManager sharedHelpManager] findString:@"Hello"  inBook:locBookName];
```

This is a wrapper for `AHRegisterHelpBook` (which is called only once to register the help book specified in the application’s main bundle) and `AHSearch`.

## Parameters

- `query`: String to search for.
- `book`: Localized help book to search. When `nil`, all installed help books are searched.

## See Also

### Displaying Help
- [func openHelpAnchor(NSHelpManager.AnchorName, inBook: NSHelpManager.BookName?)](./openhelpanchor%28_,inbook%29.md)
  Finds and displays the text at the given anchor location in the given book.
- [NSHelpManager.AnchorName](./anchorname.md)
- [NSHelpManager.BookName](./bookname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/find(_:inbook:))*