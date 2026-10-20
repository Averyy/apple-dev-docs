# openHelpAnchor(_:inBook:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Finds and displays the text at the given anchor location in the given book.

**Availability**:
- macOS

## Declaration

```swift
func openHelpAnchor(_ anchor: NSHelpManager.AnchorName, inBook book: NSHelpManager.BookName?)
```

```objc
- (void) openHelpAnchor:(NSHelpAnchorName) anchor inBook:(NSHelpBookName) book;
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
- `book`: Help book containing the anchor. When `nil`, all installed help books are searched.

## See Also

### Displaying Help
- [func find(String, inBook: NSHelpManager.BookName?)](./find%28_,inbook%29.md)
  Performs a search for the specified string in the specified book.
- [NSHelpManager.AnchorName](./anchorname.md)
- [NSHelpManager.BookName](./bookname.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/openhelpanchor(_:inbook:))*