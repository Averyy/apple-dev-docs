# startButtonTitle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The title displayed on the start button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var startButtonTitle: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * startButtonTitle;
```

## Discussion

When the title is `nil`, the button displays a system-provided title.

## See Also

### Setting Button Titles
- [var additionalRoutesButtonTitle: String?](./additionalroutesbuttontitle.md)
  The title displayed on the routes button.
- [var overviewButtonTitle: String?](./overviewbuttontitle.md)
  The title displayed on the overview button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrippreviewtextconfiguration/startbuttontitle)*