# ExtensionConfig.Intent.UpdateMediaAffinity

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

Configuration details for your service’s update media affinity intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object ExtensionConfig.Intent.UpdateMediaAffinity
```

#### Discussion

To specify that your service only implements the required methods, provide an empty array for the `opt` property. You may omit the `opt` property if your service implements all of the optional methods.

## Properties

- `opt` ([string]): Optional intent-handling steps that [`updateMediaAffinity`](./updatemediaaffinity-data.dictionarykey.md) supports.

  **Allowed Values**: `resolveAffinityType`

## Relationships

### Inherits From
- [ExtensionEndpointConfig](../../extensionendpointconfig.md)

## See Also

### Specifying Required Headers and Supported Processing for Each Intent
- [object ExtensionConfig.Intent.AddMedia](./addmedia-data.dictionary.md)
  Configuration details for your service’s add media intent.
- [object ExtensionConfig.Intent.PlayMedia](./playmedia-data.dictionary.md)
  Configuration details for your service’s play media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfig/intent-data.dictionary/updatemediaaffinity-data.dictionary)*