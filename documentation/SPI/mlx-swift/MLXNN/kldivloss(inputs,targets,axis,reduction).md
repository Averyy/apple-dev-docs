---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/kldivloss(inputs:targets:axis:reduction:)"
framework: "mlx-swift/MLXNN"
---

# klDivLoss(inputs:targets:axis:reduction:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Computes the Kullback-Leibler divergence loss.

## Declaration

```swift
func klDivLoss(inputs: MLXArray, targets: MLXArray, axis: Int = -1, reduction: LossReduction = .none) -> MLXArray
```

#### Return Value

Computed Kullback-Leibler divergence loss

#### Discussion

Computes the following when the `reduction: .none`:

```swift
sum(exp(targets) * (targets - inputs), axis: axis)
```

##### See Also

- [Loss Functions](./losses.md)

## Parameters

- `inputs`: Log probabilities for the predicted distribution
- `targets`: Log probabilities for the target distribution
- `axis`: Distribution axis
- `reduction`: Reduction type

## See Also

### Loss Functions
- [func binaryCrossEntropy(logits: MLXArray, targets: MLXArray, weights: MLXArray?, withLogits: Bool, reduction: LossReduction) -> MLXArray](./binarycrossentropy%28logits,targets,weights,withlogits,reduction%29.md)
  Computes the binary cross entropy loss.
- [func cosineSimilarityLoss(x1: MLXArray, x2: MLXArray, axis: Int, eps: Float, reduction: LossReduction) -> MLXArray](./cosinesimilarityloss%28x1,x2,axis,eps,reduction%29.md)
  Computes the cosine similarity between the two inputs.
- [func crossEntropy(logits: MLXArray, targets: MLXArray, weights: MLXArray?, axis: Int, labelSmoothing: Float, reduction: LossReduction) -> MLXArray](./crossentropy%28logits,targets,weights,axis,labelsmoothing,reduction%29.md)
  Computes the cross entropy loss.
- [func hingeLoss(inputs: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./hingeloss%28inputs,targets,reduction%29.md)
  Computes the hinge loss between inputs and targets.
- [func huberLoss(inputs: MLXArray, targets: MLXArray, delta: Float, reduction: LossReduction) -> MLXArray](./huberloss%28inputs,targets,delta,reduction%29.md)
  Computes the Huber loss between inputs and targets.
- [func l1Loss(predictions: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./l1loss%28predictions,targets,reduction%29.md)
  Computes the L1 loss
- [func logCoshLoss(inputs: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./logcoshloss%28inputs,targets,reduction%29.md)
  Computes the log cosh loss between inputs and targets.
- [func mseLoss(predictions: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./mseloss%28predictions,targets,reduction%29.md)
  Computes the mean squared error loss.
- [func nllLoss(inputs: MLXArray, targets: MLXArray, axis: Int, reduction: LossReduction) -> MLXArray](./nllloss%28inputs,targets,axis,reduction%29.md)
  Computes the negative log likelihood loss.
- [func smoothL1Loss(predictions: MLXArray, targets: MLXArray, beta: Float, reduction: LossReduction) -> MLXArray](./smoothl1loss%28predictions,targets,beta,reduction%29.md)
  Computes the smooth L1 loss.
- [func tripletLoss(anchors: MLXArray, positives: MLXArray, negatives: MLXArray, axis: Int, p: Int, margin: Float, eps: Float, reduction: LossReduction) -> MLXArray](./tripletloss%28anchors,positives,negatives,axis,p,margin,eps,reduction%29.md)
  Computes the triplet loss for a set of anchor, positive, and negative samples. Margin is represented with alpha in the math section.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/kldivloss(inputs:targets:axis:reduction:))*