# ExtensionConfig.Intent.PlayMedia

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Configuration details for your service’s play media intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ExtensionConfig.Intent.PlayMedia
```

#### Discussion

To specify that your service only implements the required methods, provide an empty array for the `opt` property. You may omit the `opt` property if your service implements all of the optional methods.

## Properties

- `opt` ([string]): Optional intent-handling steps that [`Process a Play Media Intent`](playmedia-1g2o9.md) supports.

## Relationships

### Inherits From
- [ExtensionEndpointConfig](extensionendpointconfig.md)

## See Also

- [object ExtensionConfig.Intent.AddMedia](extensionconfig/intent-data.dictionary/addmedia-data.dictionary.md)
  Configuration details for your service’s add media intent.
- [object ExtensionConfig.Intent.UpdateMediaAffinity](extensionconfig/intent-data.dictionary/updatemediaaffinity-data.dictionary.md)
  Configuration details for your service’s update media affinity intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfig/intent-data.dictionary/playmedia-data.dictionary)*