# musicSubscriptionOffer(isPresented:options:onLoadCompletion:)

**Framework**: MusicKit  
**Kind**: method

Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
nonisolated
func musicSubscriptionOffer(isPresented: Binding<Bool>, options: MusicSubscriptionOffer.Options = .default, onLoadCompletion: @escaping ((any Error)?) -> Void = { _ in }) -> some View
```

#### Discussion

The example below displays a simple button that the user can activate to begin presenting subscription offers for Apple Music. The action handler of this button initiates the presentation of those offers by setting the `isShowingOffer` variable to `true`.

```swift
struct MusicSubscriptionOfferButton: View {
    @State var isShowingOffer = false
    var body: some View {
        Button("Apple Music Subscription Offer") {
            isShowingOffer = true
        }
        .musicSubscriptionOffer(isPresented: $isShowingOffer)
    }
}
```

You can also configure the Apple Music subscription offer by creating an instance of `MusicSubscriptionOffer.Options`, setting relevant properties on it, and passing it to `.musicSubscriptionOffer(…)`. For example, to present contextual offers that highlight a specific album, you can configure the subscription offer like the following:

```swift
struct MusicSubscriptionOfferButton: View {
    var album: Album
    @State var isShowingOffer = false
    @State var offerOptions = MusicSubscriptionOffer.Options(
        affiliateToken: "<affiliate_token>", 
        campaignToken: "<campaign_token>"
    )

    var body: some View {
        Button("Apple Music Subscription Offer") {
            offerOptions.itemID = album.id
            isShowingOffer = true
        }
        .musicSubscriptionOffer(
            isPresented: $isShowingOffer, 
            options: offerOptions
        )
    }
}
```

The initial value of `offerOptions` includes relevant tokens (affiliate and campaign tokens) that allow you to receive compensation for referring new Apple Music subscribers. For more information, see this presentation of the [`Apple Services Performance Partners Program`](https://developer.apple.comhttps://affiliate.itunes.apple.com/resources/).

You may also set `isShowingOffer` to `false` to programmatically dismiss the subscription offer (or to abort its loading process).

## Parameters

- `isPresented`: A binding to a Boolean value that you can set to    to show a sheet with subscription offers for Apple Music.
- `options`: Options to use for loading the subscription offer for   Apple Music.
- `onLoadCompletion`: The function to call upon completing the initial   loading process for this subscription offer. The subscription   offer UI becomes visible when it calls this function with the   error argument as  . If there is an error in the   loading process, the subscription offer calls this function with   a non-  error, and it resets the   binding   to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/musicsubscriptionoffer(ispresented:options:onloadcompletion:))*