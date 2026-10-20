# AddMediaMediaDestinationResolutionResult.Disambiguation

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary  
**Role**: Object

A result that requires the user to choose which library or playlist they want to add media items to.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
object AddMediaMediaDestinationResolutionResult.Disambiguation
```

## Properties

- `mediaDestinationsToDisambiguate` ([MediaDestination]) *(required)*: Destinations that might match the user’s intent.

## See Also

### Clarifying a Possible Match
- [object AddMediaMediaDestinationResolutionResult.ConfirmationRequired](./confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the library or playlist before you add media items to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/addmediamediadestinationresolutionresult/disambiguation-data.dictionary)*