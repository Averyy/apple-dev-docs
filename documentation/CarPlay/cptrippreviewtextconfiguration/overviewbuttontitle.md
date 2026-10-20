# overviewButtonTitle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The title displayed on the overview button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var overviewButtonTitle: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * overviewButtonTitle;
```

#### Discussion

When the title is `nil`, the button displays a system-provided title.

## See Also

### Setting Button Titles
- [var startButtonTitle: String?](./startbuttontitle.md)
  The title displayed on the start button.
- [var additionalRoutesButtonTitle: String?](./additionalroutesbuttontitle.md)
  The title displayed on the routes button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptrippreviewtextconfiguration/overviewbuttontitle)*