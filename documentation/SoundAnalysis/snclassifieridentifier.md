# SNClassifierIdentifier

**Framework**: Sound Analysis  
**Kind**: struct  
**Role**: Structure

An identifier that represents the versions of the framework’s sound classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SNClassifierIdentifier
```

```c
typedef NSString * SNClassifierIdentifier;
```

## Topics

### Selecting a Sound Classifier
- [static let version1: SNClassifierIdentifier](./snclassifieridentifier/version1.md)
  Version 1 of the sound classifier.
### Creating an Identifier
- [init(rawValue: String)](./snclassifieridentifier/init%28rawvalue%29.md)
  Creates an identifier for a sound classifier.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Request
- [init(mlModel: MLModel) throws](./snclassifysoundrequest/init%28mlmodel%29-6rmee.md)
  Creates a request that uses a custom sound classification model.
- [init(classifierIdentifier: SNClassifierIdentifier) throws](./snclassifysoundrequest/init%28classifieridentifier%29.md)
  Creates a request that uses the framework’s built-in sound classification model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassifieridentifier)*