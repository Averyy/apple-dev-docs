# defaultContentConfiguration

**Framework**: UIKit  
**Kind**: method

Retrieves a default list content configuration for the cell’s style.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
- (UIListContentConfiguration *) defaultContentConfiguration;
```

#### Return Value

A default list content configuration. The system determines default values for the configuration according to the section where the cell appears.

#### Discussion

The default content configuration has preconfigured default styling, but doesn’t contain any content. After you get the default configuration, you assign your content to it, customize any other properties, and assign it to the cell as the current content configuration.

**Swift**:

```swift
var content = cell.defaultContentConfiguration()

// Configure content.
content.image = UIImage(systemName: "star")
content.text = "Favorites"

// Customize appearance.
content.imageProperties.tintColor = .purple

cell.contentConfiguration = content
```

**Objective-C**:

```objc
UIListContentConfiguration *content = [cell defaultContentConfiguration];

// Configure content.
[content setImage:[UIImage systemImageNamed:@"star"]];
[content setText:@"Favorites"];

// Customize appearance.
[content.imageProperties setTintColor:[UIColor purpleColor]];

[cell setContentConfiguration:content];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/defaultcontentconfiguration)*