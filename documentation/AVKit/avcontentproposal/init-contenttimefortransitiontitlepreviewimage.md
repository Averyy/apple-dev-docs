# init(contentTimeForTransition:title:previewImage:)

**Framework**: AVKit  
**Kind**: init

Creates a new content proposal with the specified transition time, title, and preview image.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
init(contentTimeForTransition: CMTime, title: String, previewImage: UIImage?)
```

#### Return Value

A new instance of [`AVContentProposal`](avcontentproposal.md).

#### Discussion

You specify the content proposal’s presentation time within the asset’s timeline. For instance, if you wanted to present the next content proposal 15 seconds before the end of the currently playing asset, you could create the next content proposal as follows:

```swift
let episode1Asset = // Currently presented asset for Episode 1
// Subtract 15 seconds from the current episode's duration
let time = episode1Asset.duration - CMTime(value: 15, timescale: 1)
let title = "My Series: Episode 2"
let image = UIImage(named: "myseries_ep2")
let proposal = AVContentProposal(contentTimeForTransition: time,
                                 title: title,
                                 previewImage: image)
// Set the proposal as the nextContentProposal of the current player item
currentPlayerItem.nextContentProposal = proposal
```

## Parameters

- `contentTimeForTransition`: A   value at which to present the content propsal within the media’s timeline.
- `title`: The title of the proposed content.
- `previewImage`: The preview image for the proposed item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentproposal/init(contenttimefortransition:title:previewimage:))*