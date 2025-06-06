# contextHelp(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the context-sensitive help for the specified key from the bundle’s help file.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func contextHelp(forKey key: NSHelpManager.ContextHelpKey) -> NSAttributedString?
```

#### Return Value

The help string or `nil` if the application does not have a `Help.plist` file or the file does not contain an entry for the specified `key`.

#### Discussion

When you build your application, you can merge multiple RTF-based help files together using the `/usr/bin/compileHelp` tool, which then packages your help file information into a property list named `Help.plist`. After placing this property-list file in your application bundle, you can use this method to extract context help information from it. To look up a particular entry, you specify the name of the original RTF help file in the `key` parameter of this method. For example, if your application project contains a help file named `Copy.rtf`, you would retrieve the text from this file by passing the value `@"Copy.rtf"` to the `key` parameter.

This method is declared in `NSHelpManager.h`.

## Parameters

- `key`: A key in your application’s   file that identifies the context-sensitive help to return.

## See Also

- [@MainActor func contextHelp(for object: Any) -> NSAttributedString?](../AppKit/NSHelpManager/contextHelp(for:).md)
  Returns context-sensitive help for an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/contexthelp(forkey:))*