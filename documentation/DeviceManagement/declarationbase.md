# DeclarationBase

**Framework**: Device Management  
**Kind**: dictionary

Keys common to all declarations used with the Remote Management protocol.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object DeclarationBase
```

#### Discussion

##### Reason Codes

- `Error.ActivationFailed`: A configuration or asset cannot be activated due to an activation that failed. - `Identifier`: (string) The `Identifier` of the declaration.
- `ServerToken`: (string) The `ServerToken` of the declaration.
- `Error.AssetCannotBeDeserialized`: The asset data does not conform to the expected data type. - `Error`: (string) Description of the underlying NSError.
- `Error.AssetCannotBeDownloaded`: The asset data cannot be downloaded. - `Error`: (string) Description of the underlying NSError.
- `Error.AssetCannotBeVerified`: The downloaded asset data cannot be verified. - `Error`: (string) Description of the underlying NSError.
- `Error.ConfigurationCannotBeApplied`: The configuration cannot be applied to the device. - `Error`: (string) Description of the underlying NSError.
- `Error.ConfigurationCannotBeDeserialized`: The configuration is not valid. - `Error`: (string) Description of the underlying NSError.
- `Error.ConfigurationFailed`: An asset cannot be activated due to a configuration that failed. - `Identifier`: (string) The `Identifier` of the declaration.
- `ServerToken`: (string) The `ServerToken` of the declaration.
- `Error.ConfigurationIsInvalid`: The configuration is not valid for applying to the device. - `Error`: (string) Description of the underlying NSError.
- `Error.ConfigurationNotSupported`: The configuration is not supported for this platform, scope, or enrollment type. - `Identifier`: (string) The `Identifier` of the configuration.
- `ServerToken`: (string) The `ServerToken` of the configuration.
- `Error.InvalidPayload`: A declaration is not fully loaded. - `Identifier`: (string) The `Identifier` of the declaration.
- `ServerToken`: (string) The `ServerToken` of the declaration.
- `Error.MissingAssets`: A configuration being activated references assets that are not present. - `Identifier`: (string) The `Identifier` of the configuration.
- `ServerToken`: (string) The `ServerToken` of the configuration.
- `AssetIdentifiers`: (array) Array of strings containing each missing asset `Identifier` value.
- `Error.MissingConfigurations`: An activation being activated references configurations that are not present. - `Identifier`: (string) The `Identifier` of the activation.
- `ServerToken`: (string) The `ServerToken` of the activation.
- `ConfigurationIdentifiers`: (array) Array of strings containing each missing configuration `Identifier` value.
- `Error.MissingState`: A declaration is missing internal state information. - `Identifier`: (string) The `Identifier` of the declaration.
- `ServerToken`: (string) The `ServerToken` of the declaration.
- `Error.PredicateFailed`: A predicate evaluation failed. - `Identifier`: (string) The `Identifier` of the activation whose predicate failed.
- `ServerToken`: (string) The `ServerToken` of the activation whose predicate failed.
- `Predicate`: (string) The predicate description of the predicate that failed.
- `Domain`: (string) Underlying NSError’s domain.
- `Code`: (string) Underlying NSError’s code.
- `Error.UnableToEvaluatePredicate`: A predicate cannot be evaluated. - `Identifier`: (string) The `Identifier` of the activation whose predicate failed to evaluate.
- `ServerToken`: (string) The `ServerToken` of the activation whose predicate failed to evaluate.
- `Predicate`: (string) The predicate description of the predicate that failed to evaluate.
- `Error.UnableToParsePredicate`: A predicate expression cannot be parsed. - `Identifier`: (string) The `Identifier` of the activation whose predicate failed to parse.
- `ServerToken`: (string) The `ServerToken` of the activation whose predicate failed to parse.
- `Predicate`: (string) The predicate description of the predicate that failed to parse.
- `Error.UnableToParsePredicateWithCustomOperator`: A predicate expression with a custom operator cannot be parsed. - `Identifier`: (string) The `Identifier` of the activation whose predicate failed to parse.
- `ServerToken`: (string) The `ServerToken` of the activation whose predicate failed to parse.
- `Predicate`: (string) The predicate description of the predicate that failed to parse.
- `Error.Unknown`: An unrecognized NSError was generated. - `Domain`: (string) NSError’s domain.
- `Code`: (string) NSError’s code.
- `Error.UnknownDeclarationType`: The declaration type is not known. - `UnknownDeclarationType`: (string) The `Type` of the declaration.
- `Error.UnknownPayloadKeys`: A declaration contains unknown payloads keys. - `UnknownPayloadKeys`: (array) Array of strings containing each unknown key-path.
- `Info.NotReferencedByActivation`: A configuration is not referenced in any activation. - `Identifier`: (string) The `Identifier` of the configuration.
- `ServerToken`: (string) The `ServerToken` of the configuration.
- `Info.NotReferencedByConfiguration`: An asset is not referenced in any configuration. - `Identifier`: (string) The `Identifier` of the asset.
- `ServerToken`: (string) The `ServerToken` of the asset.
- `Info.Predicate`: A predicate evaluated to false. - `Identifier`: (string) The `Identifier` of the activation whose predicate is false.
- `ServerToken`: (string) The `ServerToken` of the activation whose predicate is false.
- `Predicate`: (string) The predicate description of the predicate that is false.
- `Info.UnsupportedSettings`: Unsupported settings in a configuration. - `Settings`: (array) Array of strings containing each unsupported setting key-path.

## Topics

### Dictionaries
- [object DeclarationBase.Payload](declarationbase/payload-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarationbase)*