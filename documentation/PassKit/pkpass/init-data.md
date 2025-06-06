# init(data:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a pass using the data you provide.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(data: Data) throws
```

#### Discussion

If there’s a problem encoding the data you supply, this method sets the `error` parameter based on the type of problem:

- The pass contains invalid data—this method throws the [`PKPassKitError.Code.invalidDataError`](pkpasskiterror/code/invaliddataerror.md) error.
- The signature of the pass is invalid—this method throws the [`PKPassKitError.Code.invalidSignature`](pkpasskiterror/code/invalidsignature.md) error.
- For other types of errors, `/PassKit/PKPassKitError/localizedDescription` contains a string suitable for presentation to the user.

Check the console for more detailed information.

## Parameters

- `data`: A signed pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpass/init(data:))*