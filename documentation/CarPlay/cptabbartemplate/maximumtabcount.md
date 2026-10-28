# maximumTabCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum number of tabs that the template can display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class var maximumTabCount: Int { get }
```

```objc
@property (class, nonatomic, readonly) NSInteger maximumTabCount;
```

## Discussion

This property’s value depends on the app’s entitlements. At runtime, use this value to determine the maximum number of tabs that your tab bar can display.

## See Also

### Managing the Templates
- [var templates: [CPTemplate]](./templates.md)
  The tab bar’s templates.
- [func updateTemplates([CPTemplate])](./updatetemplates%28_%29.md)
  Adds, removes, reorders, or updates the tab bar’s templates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptabbartemplate/maximumtabcount)*