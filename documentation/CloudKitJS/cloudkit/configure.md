# configure

**Framework**: CloudKit JS  
**Kind**: method

Configures CloudKit JS.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
CloudKit configure(
	CloudKit.CloudKitConfig config
);
```

#### Return Value

The configured CloudKit object.

#### Discussion

For each container that you access, specify the container ID, API token, and environment.

```javascript
CloudKit.configure({
    containers: [{
        containerIdentifier: '[insert your container ID here]',
        apiTokenAuth: {
            apiToken: '[insert your API token and other authentication properties here]'
        },
        environment: 'development'
    }]
});
```

Other [`CloudKit.ContainerConfig`](cloudkit.containerconfig.md).`apiTokenAuth` keys, such as the `persist` key, are optional. To keep the user signed in after closing and reopening the browser, set `persist` to `true`.

```javascript
CloudKit.configure({
    containers: [{
        // ...
        apiTokenAuth: {
            apiToken: '[insert your API token and other authentication properties here]',
            persist: true
        }
    }]
});
```

To customize the sign in and sign out buttons, add `signInButton` and `signOutButton` keys to the `auth` dictionary.

For more container and service configuration options, see [`CloudKit.CloudKitConfig`](cloudkit.cloudkitconfig.md) in [`CloudKit JS Data Types`](cloudkit-js-data-types.md).

## Parameters

- `config`: The properties to use to initialize CloudKit JS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit/configure)*