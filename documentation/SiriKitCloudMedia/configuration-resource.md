# Configure Your Service Endpoints

**Framework**: SiriKit Cloud Media  
**Kind**: httpRequest

Provide configuration details for your media server’s endpoints to a HomePod speaker or an Apple TV.

**Availability**:
- SiriKit Cloud Media 1.0.2+

#### Discussion

You must cryptographically sign your configuration endpoint response in JSON Web Signature (JWS) format when communicating with the SiriKit Cloud Media API via [`Media Setup`](https://developer.apple.com/documentation/MediaSetup). JWS is part of the JSON Object Signing and Encryption (JOSE) open standard ([`RFC 7515`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7515)) that defines a way to cryptographically sign transmitted data.

To generate a signed JWS:

- Create the JWS header.
- Create the JWS payload.
- Sign the JWS.

To create a JWS to communicate with the SiriKit Cloud Media API, use the following fields and values in the header:

| Header | Description |
| --- | --- |
| `alg` | The algorithm used to sign the JWS. For SiriKit Cloud Media, use `ES256`. |
| `kid` | Your app bundle identifier registered for the service. |
| `typ` | The type used by the complete JWS. For SiriKit Cloud Media, use `JOSE`. |
| `cty` | The content type used by the payload of the JWS. For SiriKit Cloud Media, use `JSON`. |

The JWS payload contains JSON-encoded information specific to the SiriKit Cloud Media API and your app, such as intent type, media queues, base URLs for endpoints, and supported API version. The format is defined in the SiriKit Cloud Media [`OpenAPI Specification`](https://developer.apple.comhttps://developer.apple.com/sample-code/siri/sirikit-cloud-media-open-api.zip). Here are the major keys in the configuration data:

| Key | Description |
| --- | --- |
| `intent` | This is a mapping of (abbreviated) Intent names to the SiriKit Cloud Media endpoints and configuration options supported by web endpoint handlers. |
| `media` | This is a mapping of queue API endpoints for the particular configuration valid for the service (or user). |
| `url` | The base URL for endpoints. This value can be a fully qualified URL, or a relative URL,  used to retrieve this configuration resource. |
| `version` | The supported version of the SiriKit Cloud Media API. |

After creating the JWS, sign it using the Elliptic Curve Digital Signature Algorithm (ECDSA) with the P-256 curve and the SHA-256 hash algorithm. The SiriKit Cloud Media API identifies the intents and media endpoints your service supports by parsing the configuration response. In the decoded JWS below, the service is configured to support the add media, play media, and update media affinity intents, and provides URLs to each as well as the media queue endpoints used to handle intent responses:

```json
{
  "alg": "ES256",
  "kid": "com.myCompany.appName",
  "typ": "JOSE",
  "cty": "JSON"
}
{
  "intent": {
    "addMedia": {
      "opt": [
        "confirm",
        "resolveMediaDestination"
      ],
      "url": "intent/addMedia"
    },
    "playMedia": {
      "opt": [
        "resolvePlayShuffled",
        "resolvePlaybackRepeatMode",
        "resolvePlaybackQueueLocation",
        "resolveResumePlayback"
      ],
      "url": "intent/playMedia"
    },
    "updateMediaAffinity": {
      "url": "intent/updateMediaAffinity"
    }
  },
  "media": {
    "queues": {
      "playMedia": {
        "url": "queues/playMedia"
      },
      "updateActivity": {
        "url": "queues/updateActivity"
      }
    }
  },
  "version": "1.0.2"
}
```

Regardless of the programming language you’re using with the SiriKit Cloud Media API, there are a variety of open source libraries available online for creating and signing JWS data. Please verify and validate your response before sending it to the SiriKit Cloud Media API.

## See Also

- [type ExtensionConfigTag](extensionconfigtag.md)
  A unique identifier for a specific media service configuration.
- [object ExtensionConfig](extensionconfig.md)
  Instructions for accessing your media service’s endpoints.
- [object PlayMediaControlActivity](playmediacontrolactivity.md)
  Options for reporting playback progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/configuration-resource)*