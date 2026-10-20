# actions

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The list of actions available on the action sheet.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var actions: [CPAlertAction] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<CPAlertAction *> * actions;
```

#### Discussion

The array must include at least one action.

## See Also

### Getting Action Sheet Template Information
- [var title: String?](./title.md)
  The title of the action sheet.
- [var message: String?](./message.md)
  The descriptive message providing details about the reason for displaying the action sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpactionsheettemplate/actions)*