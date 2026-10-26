# setTitleWithMnemonic:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the cell title and mnemonic character.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```objc
- (void) setTitleWithMnemonic:(NSString *) stringWithAmpersand;
```

#### Discussion

Mnemonics are not supported in macOS.

## Parameters

- `stringWithAmpersand`: The title of the cell, including a mnemonic identifier. To specify the mnemonic character, place an ampersand (`&`) in the front of the desired character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/settitlewithmnemonic:)*