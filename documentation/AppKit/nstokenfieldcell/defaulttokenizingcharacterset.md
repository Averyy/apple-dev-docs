# defaultTokenizingCharacterSet

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the default tokenizing character set.

**Availability**:
- macOS

## Declaration

```swift
class var defaultTokenizingCharacterSet: CharacterSet { get }
```

```objc
@property (class, copy, readonly) NSCharacterSet * defaultTokenizingCharacterSet;
```

## Return Value

The default tokenizing character set.

## Discussion

The default tokenizing character set contains the single character “`,`”.

## See Also

### Managing the Tokenizing Character Set
- [var tokenizingCharacterSet: CharacterSet!](./tokenizingcharacterset.md)
  The receiver’s tokenizing character set to a given character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstokenfieldcell/defaulttokenizingcharacterset)*