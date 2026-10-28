# menu(for:string:options:atLocation:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Provides a menu containing contextual menu items suitable for certain kinds of detected results.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func menu(for result: NSTextCheckingResult, string checkedString: String, options: [NSSpellChecker.OptionKey : Any]? = nil, atLocation location: NSPoint, in view: NSView) -> NSMenu?
```

```objc
- (NSMenu *) menuForResult:(NSTextCheckingResult *) result string:(NSString *) checkedString options:(NSDictionary<NSString *,id> *) options atLocation:(NSPoint) location inView:(NSView *) view;
```

## Return Value

A menu suitable for displaying as a contextual menu, or adding to another contextual menu as a submenu.

## Parameters

- `result`: The [`NSTextCheckingResult`](../../Foundation/nstextcheckingresult.md) instance for the checked string.
- `checkedString`: The string that has been checked.
- `options`: The options dictionary allows clients to pass in information associated with the document. See `Spell Checking Option Dictionary Keys` for possible key-value pairs.
- `location`: The location, in the view’s coordinate system, to display the menu.
- `view`: The view object over which to display the contextual menu.

## See Also

### Data Detector Interaction
- [NSSpellChecker.OptionKey](./optionkey.md)
  Constants that define options for text checking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/menu(for:string:options:atlocation:in:))*