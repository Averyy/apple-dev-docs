# init(title:gridButtons:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a grid template with a title and a set of buttons.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(title: String?, gridButtons: [CPGridButton])
```

```objc
- (instancetype) initWithTitle:(NSString *) title gridButtons:(NSArray<CPGridButton *> *) gridButtons;
```

## Return Value

A newly initialized grid template.

## Parameters

- `title`: The title shown in the grid template’s navigation bar.
- `gridButtons`: An array of grid buttons to display on the template.

## See Also

### Creating a grid template
- [class var maximumGridButtonImageSize: CGSize](./maximumgridbuttonimagesize.md)
  The expected image size for your @c CPGridButton.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpgridtemplate/init(title:gridbuttons:))*