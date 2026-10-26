# init(archivalStringValue:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Archival string can be used to serialize and deserialize the PHCloudIdentifier (Note the archival format is compatible with strings archived via the deprecated API `stringValue`)

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+

## Declaration

```swift
init?(archivalStringValue archivalString: String)
```

```objc
- (instancetype) initWithArchivalStringValue:(NSString *) archivalString;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcloudidentifier/init(archivalstringvalue:))*