# init(templates:)

**Framework**: CarPlay  
**Kind**: init

Creates a tab bar template that displays the provided root templates as tabs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
init(templates: [CPTemplate])
```

#### Discussion

At runtime, use [`maximumTabCount`](cptabbartemplate/maximumtabcount.md) to determine the maximum number of tabs the template can display. CarPlay throws an exception if the number of items in `templates` exceeds this value.

CarPlay treats the array’s templates as root templates, each with its own navigation hierarchy. When a tab bar template is the [`rootTemplate`](cpinterfacecontroller/roottemplate.md) of your app’s interface controller, and you use the controller to add and remove templates, CarPlay applies those changes to the selected tab’s navigation hierarchy.

CarPlay restricts the type of template you can use as a tab’s root template according to your app’s entitlements. Audio apps can use List and Grid templates only. All other categories of apps can use List, Grid, and Information templates as a tab’s root template. In addition, EV-charging, parking, and food ordering apps can use the Point of Interest template as a root template. These restrictions apply only to a tab’s root template. You can add other template types, like the Contact or Now Playing templates, on top of a tab’s root template using the methods that [`CPInterfaceController`](cpinterfacecontroller.md) provides.

## Parameters

- `templates`: An array of templates to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptabbartemplate/init(templates:))*