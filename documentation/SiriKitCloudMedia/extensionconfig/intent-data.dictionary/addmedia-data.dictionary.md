# ExtensionConfig.Intent.AddMedia

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

Configuration details for your service’s add media intent.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object ExtensionConfig.Intent.AddMedia
```

## Discussion

To specify that your service only implements the required methods, provide an empty array for the `opt` property. You may omit the `opt` property if your service implements all of the optional methods.

## Properties

- `opt` ([string]): Optional intent-handling steps that [`Process an Add Media Intent`](../../addmedia.md) supports.

  **Allowed Values**: `resolveMediaDestination`, `confirm`

## Relationships

### Inherits From
- [ExtensionEndpointConfig](../../extensionendpointconfig.md)

## See Also

### Specifying Required Headers and Supported Processing for Each Intent
- [object ExtensionConfig.Intent.PlayMedia](./playmedia-data.dictionary.md)
  Configuration details for your service’s play media intent.
- [object ExtensionConfig.Intent.UpdateMediaAffinity](./updatemediaaffinity-data.dictionary.md)
  Configuration details for your service’s update media affinity intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfig/intent-data.dictionary/addmedia-data.dictionary)*