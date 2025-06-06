# menu(for:string:options:atLocation:in:)

**Framework**: AppKit  
**Kind**: method

Provides a menu containing contextual menu items suitable for certain kinds of detected results.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func menu(for result: NSTextCheckingResult, string checkedString: String, options: [NSSpellChecker.OptionKey : Any]? = nil, atLocation location: NSPoint, in view: NSView) -> NSMenu?
```

#### Return Value

A menu suitable for displaying as a contextual menu, or adding to another contextual menu as a submenu.

## Parameters

- `result`: The   instance for the checked string.
- `checkedString`: The string that has been checked.
- `options`: The options dictionary allows clients to pass in information associated with the document. See   for possible key-value pairs.
- `location`: The location, in the view’s coordinate system, to display the menu.
- `view`: The view object over which to display the contextual menu.

## See Also

- [NSSpellChecker.OptionKey](nsspellchecker/optionkey.md)
  The constants are optional keys that can be used in the options dictionary parameter of the [`check(_:range:types:options:inSpellDocumentWithTag:orthography:wordCount:)`](nsspellchecker/check(_:range:types:options:inspelldocumentwithtag:orthography:wordcount:).md), [`requestChecking(of:range:types:options:inSpellDocumentWithTag:completionHandler:)`](nsspellchecker/requestchecking(of:range:types:options:inspelldocumentwithtag:completionhandler:).md), and [`menu(for:string:options:atLocation:in:)`](nsspellchecker/menu(for:string:options:atlocation:in:).md) methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/menu(for:string:options:atlocation:in:))*