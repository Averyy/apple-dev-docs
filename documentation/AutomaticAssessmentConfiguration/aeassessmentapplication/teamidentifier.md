# teamIdentifier

**Framework**: Automatic Assessment Configuration  
**Kind**: property  
**Role**: Instance Property

The team identifier of the app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var teamIdentifier: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * teamIdentifier;
```

#### Discussion

You can get the team identifier for an app using the `codesign` command line utility:

```shell
% codesign -v -d /Applications/MyApp.app
```

## See Also

### Creating an assessment application
- [init(bundleIdentifier: String, teamIdentifier: String?)](./init%28bundleidentifier,teamidentifier%29.md)
  Creates a representation of an app using its bundle and team identifiers.
- [init(bundleIdentifier: String)](./init%28bundleidentifier%29.md)
  Creates a representation of an app using its bundle identifier.
- [var bundleIdentifier: String](./bundleidentifier.md)
  The bundle identifier of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentapplication/teamidentifier)*