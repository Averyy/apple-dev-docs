---
url: https://developer.apple.com/design/human-interface-guidelines/lockups
framework: HIG
---

# Lockups

**Type:** article

**Platforms:** tvos

Lockups combine multiple separate views into a single, interactive unit.

![A stylized representation of a person icon above a line of headline text and a line of footnote text. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/f3fef1aa129a89cf20704b8bab354e11/components-lockups-intro~dark%402x.png)
Each lockup consists of a content view, a header, and a footer. Headers appear above the main content for a lockup, and footers appear below the main content. All three views expand and contract together as the lockup gets focus.
According to the needs of your app, you can combine four types of lockup: cards, caption buttons, monograms, and posters.

## Best practices
**Allow adequate space between lockups.** A focused lockup expands in size, so leave enough room between lockups to avoid overlapping or displacing other lockups. For guidance, see [Layout](layout.md).
![An illustration showing three rows of five equally spaced lockups. In each row, the middle lockup is in focus and slightly larger than the others.](https://docs-assets.developer.apple.com/published/e80ddfafdbd9a59cf960d37573ea3864/lockups-generic~dark%402x.png)
**Use consistent lockup sizes within a row or group.** A group of buttons or a row of content images is more visually appealing when the widths and heights of all elements match.
For developer guidance, see [TVLockupView](../TVUIKit/TVLockupView.md) and [TVLockupHeaderFooterView](../TVUIKit/TVLockupHeaderFooterView.md).

## Cards
A card combines a header, footer, and content view to present ratings and reviews for media items.
![An illustration of an Apple TV screen that contains several cards, one of which is highlighted. Inside the highlighted card from the top, placeholder content shows the position of a rating and multiple lines of text.](https://docs-assets.developer.apple.com/published/80f9424fbccaba108aab286ac27d4511/lockups-background~dark%402x.png)
For developer guidance, see [TVCardView](../TVUIKit/TVCardView.md).

## Caption buttons
A caption button can include a title and a subtitle beneath the button. A caption button can contain either an image or text.
Make sure that when people focus on them, caption buttons tilt with the motion that they swipe. When aligned vertically, caption buttons tilt up and down. When aligned horizontally, caption buttons tilt left and right. When displayed in a grid, caption buttons tilt both vertically and horizontally.
![An illustration of an Apple TV screen highlighted to show four caption buttons in a row. The leftmost button is focused, making it expand slightly and appear to float above the background.](https://docs-assets.developer.apple.com/published/fd32589fdbeb138404933482c7c27abb/lockups-caption-button~dark%402x.png)
For developer guidance, see [TVCaptionButtonView](../TVUIKit/TVCaptionButtonView.md).

## Monograms
Monograms identify people, usually the cast and crew for a media item. Each monogram consists of a circular picture of the person and their name. If an image isn’t available, the person’s initials appear in place of an image.
**Prefer images over initials.** An image of a person creates a more intimate connection than text.
![An illustration of an Apple TV screen that contains a row of several monograms, of which the leftmost one is highlighted. Each monogram contains the person symbol. Below each monogram is placeholder content that represents two lines of text.](https://docs-assets.developer.apple.com/published/e8723b67c32f86897d908c0bd32380ed/lockups-monogram~dark%402x.png)
For developer guidance, see [TVMonogramContentView](../TVUIKit/TVMonogramContentView.md).

## Posters
Posters consist of an image and an optional title and subtitle, which are hidden until the poster comes into focus. Posters can be any size, but the size needs to be appropriate for their content. For related guidance, see [Image views](image-views.md).
![An illustration of an Apple TV screen that shows a row of several posters near the bottom edge. One poster is focused and below it is placeholder content that represents a line of text.](https://docs-assets.developer.apple.com/published/076fb3d7947bafb01d8c16e2a303639b/lockups-poster~dark%402x.png)
For developer guidance, see [TVPosterView](../TVUIKit/TVPosterView.md).

## Platform considerations
*Not supported in iOS, iPadOS, macOS, visionOS, or watchOS.*

## Resources

#### Related
[Designing for tvOS](designing-for-tvos.md)
[Layout](layout.md)

#### Developer documentation
[TVLockupView](../TVUIKit/TVLockupView.md) — TVUIKit
[TVLockupHeaderFooterView](../TVUIKit/TVLockupHeaderFooterView.md) — TVUIKit



---
*Source: [https://developer.apple.com/design/human-interface-guidelines/lockups](https://developer.apple.com/design/human-interface-guidelines/lockups)*
